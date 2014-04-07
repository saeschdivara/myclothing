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

myServices.factory('ClothingTime', ['$resource', ($resource) ->
    return $resource('/crud/clothing-time/', {'pk': '@pk'}, () ->)
])


clothingApp.controller('ClothingTimeController', ['$scope', ($scope, ClothingTime) ->
    # Query returns an array of objects, MyModel.objects.all() by default
    #$scope.models = ClothingTime.query();
    $scope.headings = ['One', 'Two', 'Three'];
])