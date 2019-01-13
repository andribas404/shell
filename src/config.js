var NODE_ENV = 'production';
let baseUrl = ''
if (NODE_ENV === 'production') {
   baseUrl = 'https://person-list.herokuapp.com/api'
} else {
   baseUrl = 'http://localhost:5000/api'
}

export const apiHost = baseUrl
