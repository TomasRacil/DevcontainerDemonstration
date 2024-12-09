const { createProxyMiddleware } = require('http-proxy-middleware');

module.exports = function (app) {
    app.use(
        '/api',
        createProxyMiddleware({
            target: 'http://backend:8000/todos',
            changeOrigin: true,
            secure: false,
            pathRewrite: {
                '^/api': '' //remove /api
            },
            onProxyReq: (proxyReq, req, res) => { // Simple Logging
                console.log('[PROXY] Request:', req.url, proxyReq, res);
            },
            onProxyRes: (proxyRes, req, res) => {
                console.log('[PROXY] Response:', proxyRes.statusCode);
            }
        })
    );
};