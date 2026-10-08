import react from '@vitejs/plugin-react'
import tailwindcss from '@tailwindcss/vite'
import { defineConfig } from 'vite'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react(), tailwindcss()],
  server: {
    // 允许通过自定义域名/反向代理访问（如 ep.shuxia.site）
    allowedHosts: true,
  },
})
