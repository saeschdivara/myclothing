clothingApp.factory('ClothingTimeFactory', ['ClothingResource', (ClothingResource) ->

    class ClothingTime

      constructor: (@isVisible = false) ->

      setData: (obj) ->
        @name = obj.name
        @slug = obj.slug
        @image = obj.image
        @clothes = []

        for clothing_id in obj.clothes
            clothing_obj = ClothingResource.get(
                id: clothing_id
            )
            clothing_obj.$promise.then(
                (data) =>
                    @clothes.push( data )
            )

      setVisible: (isVisible) ->
        @isVisible = isVisible

    ClothingTimeFactory =
      $new: () ->
        return new ClothingTime()
])