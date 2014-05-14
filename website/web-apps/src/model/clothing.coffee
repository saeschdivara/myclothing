clothingApp.factory('ClothingResource', [ '$resource', ($resource) ->
    return $resource('/api/clothing/:id/',
        id: '@id'
    ,
        stripTrailingSlashes: false
    )
])