import signUpUser from './4-user-promise.js';
import uploadPhoto from './5-photo-reject.js';
export default async function handleProfileSignup(firstName, lastName, fileName) {
  const userPromise = signUpUser(firstName, lastName);
  const photoPromise = uploadPhoto(fileName);
  const [userResult, photoResult] = await Promise.allSettled([userPromise, photoPromise]);
  const results = [];
  if (userResult.status === 'fulfilled') {
    results.push({ status: 'fulfilled', value: userResult.value });
  } else {
    results.push({ status: 'rejected', value: userResult.reason });
  }
  if (photoResult.status === 'fulfilled') {
    results.push({ status: 'fulfilled', value: photoResult.value });
  } else {
    results.push({ status: 'rejected', value: photoResult.reason });
  }
  return results;
}
