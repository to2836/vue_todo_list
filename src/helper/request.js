import axios from 'axios';
import VueCookies from 'vue-cookies'

var defaultHeaders
if (VueCookies.get('token')!=null){
  defaultHeaders = {
    Accept: 'application/json',
    Authorization: 'JWT '+VueCookies.get('token').token
  };
}
else {
  defaultHeaders = {
    Accept: 'application/json',
  };
}
   
const defaultOptions = {
  method: 'get',
};

const request = (options) => {
  let cancel;

  const promise = new Promise((resolve, reject) => {
    
    axios.request({
      ...defaultOptions,
      ...options,
      cancelToken: new axios.CancelToken((c) => {
        cancel = c;
      }),
      headers: {
        ...defaultHeaders,
        ...options.headers,
      },
    }).then((res) => {
      resolve(res.data);
    }).catch((error) => {
      if (options.cancelable) {
        reject('Request canceled');
      } else {
        reject(error.response.data);
      }
    });
  });

  if (options.cancelable) {
    return {
      promise,
      cancel,
    };
  }
  return promise;
};

export { defaultHeaders as headers };
export default request;
