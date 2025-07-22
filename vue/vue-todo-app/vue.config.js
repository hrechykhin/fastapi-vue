const { defineConfig } = require('@vue/cli-service')

module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    host: '0.0.0.0',
    port: 8080,
    hot: true,
    watchFiles: {
      options: {
        poll: true,
      },
    },
    client: {
      webSocketURL: 'ws://localhost:8081/ws',  // fix WebSocket URL
    },
  },
})
