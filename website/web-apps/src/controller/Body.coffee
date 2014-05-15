clothingApp.controller('BodyController', ['$scope', 'BodyPartResource', ($scope, BodyPartResource) ->

    class BodyController

        constructor: () ->
            @head = ''
            @upper_body_part = ''
            @lower_body_part = ''
            @left_arm = ''
            @right_arm = ''
            @left_leg = ''
            @right_leg = ''

            BodyPartResource.query().$promise.then(
                (result) =>
                    @all_parts = result
            )

        $onClothingChosen: (event, message) =>
            clothing = message.clothing
            body_part_id = clothing.body_parts[0]
            body_part_object = null

            for part in @all_parts
                if part.id is body_part_id
                    body_part_object = part
                    break

            if part
                body_part_name = part.name.toLowerCase().replace(/[ ]/, '_')
                @[body_part_name] = clothing.image

                console.log(@)

    $scope.foo = 'dddd'

    $controller = new BodyController()
    $scope.$on('CLOTHING_IS_CHOSEN', $controller.$onClothingChosen)

    return $controller
])