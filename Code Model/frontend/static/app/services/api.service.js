mainApp.factory("Item", ['$resource',
    function ($resource) {
        return $resource("http://localhost:5000/api/v1/items/:id/", {id: '@id'}, {
            'update': {method: 'PUT'}
        });
    }]);

mainApp.factory("Attribute", ['$resource',
    function ($resource) {
        return $resource("http://localhost:5000/api/v1/attributes/:id/", {id: '@id'}, {
            'update': {method: 'PUT'}
        });
    }]);

mainApp.factory("Location", ['$resource',
    function ($resource) {
        return $resource("http://localhost:5000/api/v1/locations/:id/", {id: '@id'}, {
            'update': {method: 'PUT'}
        });
    }]);

mainApp.factory("OptionGroup", ['$resource',
    function ($resource) {
        return $resource("http://localhost:5000/api/v1/optiongroups/:id/", {id: '@id'}, {
            'update': {method: 'PUT'}
        });
    }]);

mainApp.factory("Option", ['$resource',
    function ($resource) {
        return $resource("http://localhost:5000/api/v1/optiongroups/:optiongroupid/options/:optionid/", {
            optiongroupid: '@optiongroupid',
            optionid: '@optionid'
        }, {
            'update': {method: 'PUT'}
        });
    }]);

mainApp.factory("ItemAttribute", ['$resource',
    function ($resource) {
        return $resource("http://localhost:5000/api/v1/items/:itemid/attributes/:attributeid", {
            itemid: '@itemid',
            attributeid: '@attributeid'
        }, {
            'update': {method: 'PUT'}
        });
    }]);

mainApp.factory("ItemVariation", ['$resource',
    function ($resource) {
        return $resource("http://localhost:5000/api/v1/items/:itemid/variations/:variationid", {
            itemid: '@itemid',
            variationid: '@variationid'
        }, {
            'update': {method: 'PUT'}
        });
    }]);
