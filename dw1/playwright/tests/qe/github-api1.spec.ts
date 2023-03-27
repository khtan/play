// * imports
import { test, expect } from '@playwright/test';
import Log from '../../common/logger';
// * comments
/*
1. The examples provided in https://playwright.dev/docs/test-api-testing are illustrative but
not good for running all the time.
2. If the beforeAll creates the repo and afterAll deletes the repo, there would be nothing to see
The check to see if the repo exists before creating is useful.
The create bug/feature report should have a date-time stamp so that the repo can be reused
3. The verification code expect(response.ok()).toBeTruthy() is fit for demo but not for
production. In production, expected status should be acknowledged and handled, unexpected
status should be failed and investigated.
4. So after creating the test-repo-1, the beforeAll code is commented out.
*/
// * consts
const log = new Log('github-api1');
const REPO = 'test-repo-1';
const USER = 'khtan';
// * beforeAll
/*
test.beforeAll(async ({ request }) => {
  // Create a new repository
  const response = await request.post('/user/repos', {
    data: {
      name: REPO
    }
  });
  expect(response.ok()).toBeTruthy();
});
*/
test.beforeAll(async () => {
  let preCheckFailed: Boolean = true;
  if ( process.env.GITHUB_API_TOKEN  === undefined ) {
    log.error(`The env variable GITHUB_API_TOKEN is undefined`)
  } else if ( process.env.GITHUB_API_TOKEN  === null ) {
    log.error(`The env variable GITHUB_API_TOKEN is null`)    
  // } else if ( process.env.GITHUB_API_TOKEN  === "" ) {
  } else if ( process.env.GITHUB_API_TOKEN.length  === 0 ) {    
    log.error(`The env variable GITHUB_API_TOKEN is empty string`)
  } else {
    log.info(`env variable GITHUB_API_TOKEN defined as ${process.env.GITHUB_API_TOKEN}`)
    preCheckFailed = false;
  }
  expect(preCheckFailed).toBeFalsy();
});
// * tests
test('should create a bug report', async ({ request }) => {
  const newIssue = await request.post(`/repos/${USER}/${REPO}/issues`, {
    data: {
      title: '[Bug] report 1',
      body: 'Bug description',
    }
  });
  expect(newIssue.ok()).toBeTruthy();

  const issues = await request.get(`/repos/${USER}/${REPO}/issues`);
  expect(issues.ok()).toBeTruthy();
  expect(await issues.json()).toContainEqual(expect.objectContaining({
    title: '[Bug] report 1',
    body: 'Bug description'
  }));
});

test('should create a feature request', async ({ request }) => {
  const newIssue = await request.post(`/repos/${USER}/${REPO}/issues`, {
    data: {
      title: '[Feature] request 1',
      body: 'Feature description',
    }
  });
  expect(newIssue.ok()).toBeTruthy();

  const issues = await request.get(`/repos/${USER}/${REPO}/issues`);
  expect(issues.ok()).toBeTruthy();
  expect(await issues.json()).toContainEqual(expect.objectContaining({
    title: '[Feature] request 1',
    body: 'Feature description'
  }));
});

test('t0-xxx', async ({ request }) => {
  const response = await request.get('');
    if ( response.ok() ) {
    log.info('get succeeded');
    const respBody = JSON.parse(await response.text());
    // log.info(`respBody = ${respBody}`); // this just prints [object Object]
    // log.info(respBody); // this will stringify the entire respBody
    log.info(`current_user_url: ${respBody.current_user_url}`);
  } else {
    log.info('get failed');
  }
});