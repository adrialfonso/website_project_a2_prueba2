import http from '../http-common'

class BookService {
  readBooks (skip = 0, limit = 100) {
    const config = {
      headers: {
        'accept': 'application/json'
      },
      params: {
        skip: skip,
        limit: limit
      }
    }

    const path = '/api/v1/books'

    return http.get(path, config)
      .then((res) => {
        return res
      })
      .catch((error) => {
        return Promise.reject(error)
      })
  }
  readTop5MatchedBooks (keyword) {
    const config = {
      headers: {
        'accept': 'application/json'
      }
    }

    const path = '/api/v1/books/' + keyword

    return http.get(path, config)
      .then((res) => {
        return res
      })
      .catch((error) => {
        return Promise.reject(error)
      })
  }

  readBookById (id) {
    const config = {
      headers: {
        'accept': 'application/json'
      }
    }
    const path = '/api/v1/books/book/' + id

    return http.get(path, config)
      .then((res) => {
        return res
      })
      .catch((error) => {
        return Promise.reject(error)
      })
  }
}

export default new BookService()
