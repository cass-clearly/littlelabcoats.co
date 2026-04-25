const fs = require('fs');
const os = require('os');
const path = require('path');
const { execFileSync } = require('child_process');
const puppeteer = require('puppeteer-core');

const repoRoot = path.resolve(__dirname, '..');
const manifestPath = path.join(repoRoot, 'ops', 'bundle-manifests.json');
const manifest = JSON.parse(fs.readFileSync(manifestPath, 'utf8'));

function resolveTargets(args) {
  if (args.length === 0) return Object.keys(manifest.bundles);
  const resolved = [];
  for (const arg of args) {
    if (manifest.groups[arg]) {
      resolved.push(...manifest.groups[arg]);
    } else if (manifest.bundles[arg]) {
      resolved.push(arg);
    } else {
      throw new Error(`Unknown bundle target: ${arg}`);
    }
  }
  return [...new Set(resolved)];
}

async function renderHtmlToPdf(inputPath, outputPath) {
  const browser = await puppeteer.launch({
    executablePath: '/usr/bin/google-chrome',
    headless: true,
    args: ['--no-sandbox', '--disable-gpu']
  });
  try {
    const page = await browser.newPage();
    await page.goto(`file://${path.resolve(repoRoot, inputPath)}`, { waitUntil: 'networkidle0', timeout: 120000 });
    await page.pdf({
      path: outputPath,
      format: 'Letter',
      printBackground: true,
      preferCSSPageSize: true,
      margin: { top: '0', right: '0', bottom: '0', left: '0' }
    });
  } finally {
    await browser.close();
  }
}

async function buildUnitBundle(sku, config) {
  const outputPath = path.join(repoRoot, config.output);
  fs.mkdirSync(path.dirname(outputPath), { recursive: true });
  const tmpDir = fs.mkdtempSync(path.join(os.tmpdir(), `${sku}-`));
  try {
    const rendered = [];
    for (let i = 0; i < config.lessons.length; i += 1) {
      const lesson = config.lessons[i];
      const pdfPath = path.join(tmpDir, `${String(i + 1).padStart(2, '0')}.pdf`);
      if (!fs.existsSync(path.join(repoRoot, lesson))) {
        throw new Error(`Missing lesson source for ${sku}: ${lesson}`);
      }
      await renderHtmlToPdf(lesson, pdfPath);
      rendered.push(pdfPath);
    }
    execFileSync('pdfunite', [...rendered, outputPath], { stdio: 'inherit' });
    return outputPath;
  } finally {
    fs.rmSync(tmpDir, { recursive: true, force: true });
  }
}

function buildCompleteBundle(sku, config) {
  const outputPath = path.join(repoRoot, config.output);
  fs.mkdirSync(path.dirname(outputPath), { recursive: true });
  const inputs = config.bundles.map(bundle => path.join(repoRoot, bundle));
  for (const input of inputs) {
    if (!fs.existsSync(input)) {
      throw new Error(`Missing child bundle for ${sku}: ${path.relative(repoRoot, input)}`);
    }
  }
  execFileSync('pdfunite', [...inputs, outputPath], { stdio: 'inherit' });
  return outputPath;
}

async function main() {
  const targets = resolveTargets(process.argv.slice(2));
  for (const sku of targets) {
    const config = manifest.bundles[sku];
    const out = config.type === 'unit'
      ? await buildUnitBundle(sku, config)
      : buildCompleteBundle(sku, config);
    console.log(`${sku}\t${path.relative(repoRoot, out)}`);
  }
}

main().catch((error) => {
  console.error(error.stack || error.message || String(error));
  process.exit(1);
});
