define([
    "underscore",
    "backbone",
    "handlebars",
    "text!templates/filter.handlebars"
], function (_, Backbone, Handlebars, tmpl) {
    var View;

    View = Backbone.View.extend({
        el: $('.filter-view'),
        
        template: Handlebars.compile(tmpl),

        events: {
            "click .filter-button": "onClickFilter",
            // "submit form#filter": "onSubmitFilter",
            'keyup input.filter-value': 'onChangeFilter'
        },

        initialize: function(options){
            this.render();
        },

        render: function () {
            var self = this;
            this.$el.html(this.template({}));
        },

        onChangeFilter: function (event) {
            var val = $(event.currentTarget).val();
            this.trigger('change', val);
        },

        onClickFilter: function (event) {
            event.preventDefault();
            console.log(event);
        },

        onSubmitFilter: function (event) {
            // this is not working because this form is contained in another form 
            // to get controls aligned. 
            event.preventDefault();
            console.log(event);
        }
    });

    return View;
})