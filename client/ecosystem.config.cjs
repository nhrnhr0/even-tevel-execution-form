
module.exports = {
    apps: [
        {
            name: 'even',
            script: './build/index.js',
            watch: false,
            ignore_watch: ['database'],
            autorestart: true,
            // ----------------------------------------------------
            // when I try to inject a .env it's just being ignored:
            // ----------------------------------------------------
            env: {
                PORT: 4000,
            }
        }
    ]
};
