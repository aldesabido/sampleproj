var app = angular.module("daily_task",['common_module','ui.router','ui.calendar']);

app.controller('daily_taskCtrl', function($scope,$http,$controller,$state,CommonFunc,CommonRead,CommonFac){
    angular.extend(this, $controller('CommonCtrl', {$scope: $scope}));
    var me = this;

    me.search_data ={}

    me.daily_task_dialog = function(record){
        me.current_record = angular.copy(record);
        me.record = {};
        me.open_dialog("/daily_task/daily_task_dialog/","dialog_height_100 dialog_width_70");
    }

    me.create = function(record){
        var record = angular.copy(record);
        record["user"] = me.current_record.id;
        var post = me.post_generic("/daily_task/create/",record,"main",true,false,true)
        post.success(function(response){
            me.read_pagination();
        })
    }

    me.delete = function(record){
        var confirmation = CommonFunc.confirmation("Continue delete?");
        console.log(record.id)
        confirmation.then(function(){
            var post = me.post_generic("/daily_task/delete/"+record.id+"/",{},"main",true)
            post.success(function(response){
                me.read_pagination();
            })
        })
    }

    me.read_pagination = function(){
        var filters = me.format_date(angular.copy(me.filters));
        var post = me.post_generic("/daily_task/read_pagination/",filters,"main")
        console.log(filters)
        post.success(function(response){
            me.records = response.data;
            me.generate_pagination(me,response);
        });
    };

    me.testing = function(){
        
        var filters = me.format_date(angular.copy(me.filters));
        console.log(filters["date_to"])
        me.search_data["date_to"] = filters["date_to"]
        me.search_data["date_from"] = filters["date_from"]
        console.log(me.search_data)
        var post = me.post_generic("/daily_task/search_user/",me.search_data,"main");
        post.success(function(response){
            console.log(response.data)
            me.records = response.data;
            me.generate_pagination(me,response);
        });
    };
    


    me.create_dialog = function(record){
        me.current_record = angular.copy(record);
        me.open_dialog("/daily_task/create_dialog/","dialog_height_100 dialog_width_70");
    }

    me.reset = function(){
        me.filters = {};
        me.filters.date_from = new Date().setDate(new Date().getDate() - 2);
        me.filters.date_to = new Date();
        me.read_pagination();
    }

    me.reset();
});