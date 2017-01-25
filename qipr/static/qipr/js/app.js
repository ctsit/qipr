
//this automatically executes
! function () {
    var facetDetailIcons = document.querySelectorAll('i.facet-tag__details');

    Array.prototype.forEach.call(facetDetailIcons, function (node) {
        node.addEventListener('click', function (event) {
            var clicked = event.target,
                siblingDetailList = clicked.parentElement.querySelector('ul.facet-tag__facet-list');
            if (clicked.classList.contains('facet-tag__details--inactive')) {
                clicked.classList.remove('facet-tag__details--inactive');
                clicked.textContent = 'remove';
                siblingDetailList.classList.remove('hidden');
            } else {
                clicked.classList.add('facet-tag__details--inactive');
                clicked.textContent = 'add';
                siblingDetailList.classList.add('hidden');
            }
        });
    });

    var facets = document.querySelectorAll('.facet-tag__input');

    try {
        var descriptors = JSON.parse(document.querySelector('#search-descriptors').textContent);
    } catch (err) {
        console.log(err);
        var descriptors = [];
    }

    function getFacetTagRoot(node) {
        if (node.classList.contains('facet-tag')) {
            return node;
        } else {
            return node.parentElement && getFacetTagRoot(node.parentElement);
        }
    }

    descriptors.forEach(function (item) {
        Array.prototype.forEach.call(facets, function (facet) {
            var filterField = facet.getAttribute('data-filterfield'),
                value = facet.getAttribute('data-value'),
                root = getFacetTagRoot(facet),
                icon,
                facetList;
            if (value === item.v && filterField === item.ff) {
                facet.checked = true;
                icon = root.querySelector('i');
                facetList = root.querySelector('ul');
                icon.classList.remove('facet-tag__details--inactive');
                facetList.classList.remove('hidden');
            }
        });
    });

    var getHostnameSuffix = function () {
        return window.location.hostname.includes('qipr.ctsi.ufl.edu') ? '/registry' : '';
    };

    var goToSearchPage = function (searchText, descriptors){
        var url = getHostnameSuffix() + '/search/s=' + searchText
                + '/' + (descriptors ? 'd=' + JSON.stringify(descriptors) : '');
        window.location.pathname = url;
    };

    var getDescriptors = function (node) {
        var descriptors = document.querySelector('#search-descriptors').textContent;

        descriptors = JSON.parse(descriptors);
        if (node.hasAttribute('data-value')){
            descriptors = addDescriptorIfNew(descriptors, node);
        }
        return descriptors;
    };

    var addDescriptorIfNew = function (descriptors, node) {
        var value = node.getAttribute('data-value'),
            filterField = node.getAttribute('data-filterfield'),
            data = {ff: filterField, v: value},
            containsDescriptor = descriptors.reduce(function(acc, item) {
                return acc || (item.v === value && item.ff === filterField);
            }, false);
        if (containsDescriptor) {
            //unchecks
            descriptors = descriptors.filter(function (item) {
                return (item.v !== value && item.ff !== value);
            });
        } else {
            //checks
            descriptors.push(data);
        }
        return descriptors;
    };

    window.searchHandler = function (event) {
        var clicked = event.target,
            searchText = document.querySelector('#search').value,
            descriptors = getDescriptors(event.target);

        goToSearchPage(searchText, descriptors);
    };

    Array.prototype.forEach.call(facets, function (node) {
        node.addEventListener('click', window.searchHandler);
    });

    try {
        document.querySelector('#search_form').addEventListener('submit', window.searchHandler);
    } catch (err) {console.log(err);};

    try {
        document.getElementById('back-to-search').addEventListener('click', function (event) {
            event.preventDefault();
            window.history.back();
            return false;
        });
    } catch (err) {console.log(err);};

}();
