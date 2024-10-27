import axios from 'axios'
import process from 'shelljs'

export default axios.create({
  baseURL: process.env.API_URL,
  withCredentials: true
})
