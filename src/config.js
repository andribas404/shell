process.env.NODE_ENV = 'production';
let baseUrl = ''
if (process.env.NODE_ENV === 'production') {
   baseUrl = 'https://person-list.herokuapp.com/api'
} else {
   baseUrl = 'http://localhost:5000/api'
}

export const apiHost = baseUrl
