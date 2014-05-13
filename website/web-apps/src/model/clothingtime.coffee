clothingApp.factory('ClothingTimeFactory', ['ClothingResource', (ClothingResource) ->

    class ClothingTime

      constructor: (@isVisible = false) ->

      setData: (obj) ->
        @name = obj.name
        @slug = obj.slug
        @image = obj.image
        @clothes = []

        for clothe_url in obj.clothes
            clothe_obj = ClothingResource.get(clothe_url)
            clothe_obj.$promise.then(
                (data) =>
                    console.log(data)
                    @clothes.push( data )
            )

      setVisible: (isVisible) ->
        @isVisible = isVisible

    ClothingTimeFactory =
      $new: () ->
        return new ClothingTime()
])