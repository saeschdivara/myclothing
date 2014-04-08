clothingApp = angular.module('clothing-app', ['ngCookies'])
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

myServices = angular.module('myServices', ['ngResource']);

myServices.factory('ClothingTime', ['$http', ($http) ->
    class ClothingTime
      test = () ->

    return ClothingTime
])

clothingApp.factory('clothingTimeManager', ['$http', '$q', ($http, $q) ->

    clothingTimeManager =
      test: 2
      loadAll: () ->
        deferred = $q.defer()
        $http.get('http://localhost:9222/api/users').success(
            (list) ->
              console.log(list)
              deferred.resolve(list)
          )
        .error(
            () ->
              deferred.reject()
          )

        deferred.promise
])


clothingApp.controller('ClothingTimeController', ['$scope', 'clothingTimeManager', ($scope, clothingTimeManager) ->
    # Load all clothing times
    clothingTimeManager.loadAll().then(
      (userList) =>
        $scope.users = userList
    )
])