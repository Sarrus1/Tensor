/**
 *
 * This script allows to transpile React elements of Tensor.
 * It will bundle and minify the file, and output them in backend/static/js.
 * Invoke it by running:
 *
 *        `node esbuild.js`
 *
 * It provides a dev and watch mode, by passing the argument
 * `dev` or `watch` when calling the script:
 *
 *        `node esbuild.js dev`
 *
 * DEV MODE: No minification, sourcemaps, no watch for changes.
 * WATCH MODE: No minification, sourcemaps, watch for changes.
 * PROD MODE: Minification and no sourcemaps.
 *
 * In order to add an entry to the file list, edit the entryPoints array.
 *
 * @summary ESBuild script file for the frontend React elements of Tensor.
 * @author Sarrus1
 * @date October 2022
 */

const path = require("path");

const appsdir = path.join(__dirname, "src");

const entryPoints = [
  "ban-add.tsx",
  "bans-list.tsx",
  "donations.tsx",
  "pollColors.tsx",
  "servers.tsx",
  "utils.tsx",
];

// Parse arguments
const watch = process.argv[2] === "watch";
const dev = process.argv[2] === "dev";

require("esbuild")
  .build({
    entryPoints: entryPoints.map((e) => path.join(appsdir, e)),
    bundle: true,
    sourcemap: dev || watch,
    minify: !dev && !watch,
    outdir: path.join(__dirname, "../backend/static/js"),
    logLevel: "info",
    watch: watch,
  })
  .catch((err) => {
    console.error(err);
    process.exit(1);
  });
