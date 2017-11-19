$(function() {
    var FIELD_TEXTAREA = {
        type: "textarea",
        itemTemplate: function(value, item) {
            return '<div style="height:40px; overflow:hidden">' + value + '</div>';
        }
    };

    $("#jsGrid").jsGrid({
        height: "500px",
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
                        console.log(item);
                        return item;
                        
                        return $.extend(item.fields, { id: item.id["_$oid"] });
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
            { name: "category", type: "text" },
            { name: "vendorNum", type: "text" },
            { name: "setNum", type: "text" },
            { name: "packetNum", type: "text" },
            { name: "questionNum", type: "text" },
            $.extend({ name: "tossupQ" }, FIELD_TEXTAREA),
            $.extend({ name: "tossupA" }, FIELD_TEXTAREA),
            $.extend({ name: "bonusQ" }, FIELD_TEXTAREA),
            $.extend({ name: "bonusA" }, FIELD_TEXTAREA),
            { type: "control" }
        ]
    });
});