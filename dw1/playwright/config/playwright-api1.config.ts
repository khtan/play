import { defineConfig } from '@playwright/test';
export default defineConfig({
    testDir: '../tests/qe',    
    testMatch: /.*(e2e-spec|spec).ts/,    
    use: {
        // All requests we send go to this API endpoint.
        baseURL: 'https://api.github.com',
        extraHTTPHeaders: {
            // We set this header per GitHub guidelines.
            'Accept': 'application/vnd.github.v3+json',
            // Add authorization token to all requests.
            // Assuming personal access token available in the environment.
            'Authorization': `token ${process.env.GITHUB_API_TOKEN}`,
        },
    }
});
