$(function() {
    $("#jsGrid").jsGrid({
        height: "50%",
        width: "100%",
        filtering: true,
        inserting: true,
        editing: true,
        sorting: true,
        paging: true,
        autoload: true,
        pageSize: 10,
        pageButtonCount: 5,
        deleteConfirm: "Do you really want to delete this question?",
        controller: {
            loadData: function(filter) {
                var d = $.Deferred();
                $.ajax({
                    type: "GET",
                    url: "/api",
                    data: filter
                }).done(function(result) {
                    d.resolve($.map(result, function(item) {
                        return $.extend(item.fields, { id: item.pk });
                    }));
                });
                return d.promise();
            },
            insertItem: function(item) {
                return $.ajax({
                    type: "POST",
                    url: "/api",
                    data: item
                });
            },
            updateItem: function(item) {
                return $.ajax({
                    type: "PUT",
                    url: "/api/" + item.id,
                    data: item
                });
            },
            deleteItem: function(item) {
                return $.ajax({
                    type: "DELETE",
                    url: "/api/" + item.id
                });
            }
        },
        fields: [
            { name: "tossupQ", type: "text", width: 150 },
            { name: "tossupA", type: "text", width: 150 },
            { name: "bonusQ", type: "text", width: 150 },
            { name: "bonusA", type: "text", width: 150 },
            { type: "control" }
        ]
    });
});