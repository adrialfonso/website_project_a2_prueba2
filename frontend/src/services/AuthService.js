import http from '../http-common'

class AuthService {
  login (username, password) {
    const parameters = 'username=' + username + '&password=' + password
    const config = {
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded'
      }
    }
    const path = '/api/v1/login/access-token/'

    return http.post(path, parameters, config)
      .then((res) => {
        return res
      })
      .catch((error) => {
        return Promise.reject(error)
      })
  }

  register (username, password, fullname) {
    const userData = {'password': password, 'email': username, 'full_name': fullname}
    const config = {
      headers: {
        'accept': 'application/json',
        'Content-Type': 'application/json'
      }
    }

    const path = '/api/v1/users'

    return http.post(path, userData, config)
      .then((res) => {
        return res
      })
      .catch((error) => {
        return Promise.reject(error)
      })
  }
}

export default new AuthService()
