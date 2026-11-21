import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";

// __dirname isn't defined in ES modules, so work it out from this file's URL
const here = path.dirname(fileURLToPath(import.meta.url));
const keyPath = path.resolve(here, "../payments-api/certs/localhost.key");
const certPath = path.resolve(here, "../payments-api/certs/localhost.crt");

// The dev certificate is git-ignored; use HTTPS when it exists (see payments-api/.env.example to create it)
const https =
  fs.existsSync(keyPath) && fs.existsSync(certPath)
    ? { key: fs.readFileSync(keyPath), cert: fs.readFileSync(certPath) }
    : undefined;

export default defineConfig({
  plugins: [react()],
  server: {
    https,
    host: "localhost",
    port: 5174, // ← you were running on 5174; keep it consistent
    proxy: {
      // Proxy API calls to Express (which should also be running with HTTPS)
      "/api": {
        target: "https://localhost:4000",
        changeOrigin: true,
        secure: false, // allow self-signed cert in dev
      },
    },
  },
});
