import http from '../http-common'

class AuthService {
  login (username, password) {
    const config = {
      headers: {
        'accept': 'application/json'
      },
      params: {
        email: username,
        pswd_input: password
      }
    }

    const path = '/api/v1/login'

    return http.post(path, null, config)
      .then((res) => {
        return res
      })
      .catch((error) => {
        return Promise.reject(error)
      })
  }

  register (email, username, password, name, surname) {
    const userData = {'password': password, 'email': email, 'username': username, 'name': name, 'surname': surname}
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
