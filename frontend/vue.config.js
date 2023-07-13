const { defineConfig } = require('@vue/cli-service')

module.exports = defineConfig({
    transpileDependencies: true,
    devServer: {
        proxy: {
            '^/api': {
                target: 'http://localhost:8000',
                ws: true,
                changeOrigin: true
            },
            '^/dj-rest-auth': {
                target: 'http://localhost:8000',
                ws: true,
                changeOrigin: true
            },
        }
    }
})