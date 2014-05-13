clothingApp.factory( 'ClothingResource', [ '$resource', ( $resource ) ->
   return $resource( 'http://0.0.0.0:9222/api/clothing/:id',  id: '@id'  )
])