clothingApp.factory('clothingTimeManager', ['$http', '$q', 'ClothingTimeFactory', ($http, $q, ClothingTimeFactory) ->

    clothingTimeManager =
      test: 2
      loadAll: () ->
        deferred = $q.defer()
        $http.get('/api/clothing-time/').success(
            (list) ->
              times = []
              for clothingTime in list
                time = ClothingTimeFactory.$new()
                time.setData(clothingTime)
                times.push( time )

              deferred.resolve(times)
          )
        .error(
            () ->
              deferred.reject()
          )

        deferred.promise

    # Return the manager
    clothingTimeManager
])


clothingApp.controller('ClothingTimeController', ['$scope', '$rootScope', 'clothingTimeManager',
    ($scope, $rootScope, clothingTimeManager) ->
        # Load all clothing times
        clothingTimeManager.loadAll().then(
          (clothingtimeList) =>
            $scope.clothingtimes = clothingtimeList
        )

        class ClothingTimeController

            constructor: () ->
                ###
                ###


            $onClothingChosen: (clothing) ->
                ###
                ###

                $rootScope.$broadcast('CLOTHING_IS_CHOSEN',
                    clothing: clothing
                )


        $controller = new ClothingTimeController()
        $scope.onClothingChosen = $controller.$onClothingChosen

        return $controller
])