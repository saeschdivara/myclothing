clothingApp.factory('clothingTimeManager', ['$http', '$q', ($http, $q) ->

    clothingTimeManager =
      test: 2
      loadAll: () ->
        deferred = $q.defer()
        $http.get('/api/clothing-time/').success(
            (list) ->
              console.log(list)
              deferred.resolve(list)
          )
        .error(
            () ->
              deferred.reject()
          )

        deferred.promise

    # Return the manager
    clothingTimeManager
])


clothingApp.controller('ClothingTimeController', ['$scope', 'clothingTimeManager', ($scope, clothingTimeManager) ->
    # Load all clothing times
    clothingTimeManager.loadAll().then(
      (clothingtimeList) =>
        $scope.clothingtimes = clothingtimeList
    )
])