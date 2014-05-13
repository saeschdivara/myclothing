window.clothingApp = angular.module('clothing-app', ['ngCookies', 'ngResource'])
.config(($interpolateProvider)  ->
    $interpolateProvider.startSymbol('{$')
    $interpolateProvider.endSymbol('$}')
  )
.run(($http, $cookies) ->
    $http.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest'
    $http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken
    # Add the following two lines
    $http.defaults.xsrfCookieName = 'csrftoken'
    $http.defaults.xsrfHeaderName = 'X-CSRFToken'
  )