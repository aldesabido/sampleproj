var app = angular.module("app",['common_module','ui.router']);

app.config(['$httpProvider', '$interpolateProvider','$stateProvider', '$urlRouterProvider', function($httpProvider, $interpolateProvider, $stateProvider, $urlRouterProvider) {

	$httpProvider.defaults.xsrfCookieName = 'csrftoken';
	$httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
	$interpolateProvider.startSymbol('{$').endSymbol('$}');

    $stateProvider
        .state('daily_task', { 
            url: '/daily_task',
            templateUrl: '/daily_task',
            controller: 'daily_taskCtrl as main',
            cache: false,
            resolve: {
                load: function ($ocLazyLoad) {
                    return $ocLazyLoad.load([
                        {
                            name: 'daily_task',
                            files: [ '/static/js/daily_task.js',]
                        },
                    ]);
                }
            }
        })

        .state('departments', { 
            url: '/departments',
            templateUrl: '/departments',
            controller: 'departmentsCtrl as main',
            cache: false,
            resolve: {
                load: function ($ocLazyLoad) {
                    return $ocLazyLoad.load([
                        {
                            name: 'departments',
                            files: [ '/static/js/departments.js',]
                        },
                    ]);
                }
            }
        })
        .state('task_types', { 
            url: '/task_types',
            templateUrl: '/task_types',
            controller: 'task_typesCtrl as main',
            cache: false,
            resolve: {
                load: function ($ocLazyLoad) {
                    return $ocLazyLoad.load([
                        {
                            name: 'task_types',
                            files: [ '/static/js/task_types.js',]
                        },
                    ]);
                }
            }
        })


    $urlRouterProvider.otherwise('daily_task');
}])

app.controller('wrapperCtrl', function($scope,$http,$controller,$state,CommonFunc,CommonRead,CommonFac){
    angular.extend(this, $controller('CommonCtrl', {$scope: $scope}));
    var me = this;
    var titles = {
        "daily_task": "Daily Tasks",
        "departments": "Departments",
    }

    $scope.$on('$stateChangeStart',function(){me.page_loader["main"] = true;})
    $scope.$on('$stateChangeSuccess',function(){
        me.page_loader["main"] = false;
        CommonFac.set_title(titles[$state.current.name]);
        me.title = CommonFac.get_title();
        me.current_page = $state.current.name;
    })
});

app.controller('dashboardCtrl', function($scope,$http,$controller,$state,CommonFunc,CommonRead,CommonFac){
    angular.extend(this, $controller('CommonCtrl', {$scope: $scope}));
    var me = this;
});

