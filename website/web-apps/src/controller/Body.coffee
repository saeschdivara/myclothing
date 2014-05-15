clothingApp.controller('BodyController', ['$scope', 'BodyPartResource', ($scope, BodyPartResource) ->

    class BodyController

        constructor: () ->
            @head = ''
            @upper_body_part = ''
            @lower_body_part = ''
            @left_arm = ''
            @right_arm = ''
            @left_foot = ''
            @right_foot = ''

            @all_parts = BodyPartResource.get()

            console.log(@all_parts)

        $onClothingChosen: (event, message) =>
            console.log(event)

    $scope.foo = 'dddd'

    $controller = new BodyController()
    $scope.$on('CLOTHING_IS_CHOSEN', $controller.$onClothingChosen)

    return $controller
])