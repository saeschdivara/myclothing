module.exports = function (grunt) {

    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        coffee: {
            compileJoined: {
                options: {
                    join: true
                },
                files: {
                    'website/web-apps/dist/controller/controllers.js': [
                        'website/web-apps/src/controller/*.coffee'
                    ],
                    'website/web-apps/dist/model/models.js': [
                        'website/web-apps/src/model/*.coffee'
                    ]
                }
            }
        },
        ngmin: {
          controllers: {
            src: ['website/web-apps/dist/controller/controllers.js'],
            dest: 'website/web-apps/dist/controller/controllers.js'
          }
        },
        uglify: {
            options: {
                banner: '/*! <%= pkg.name %> - v<%= pkg.version %> - ' +
                        '<%= grunt.template.today("yyyy-mm-dd")  %> copyright by <%= pkg.author %> */ \n',

                compress: {
                    drop_console: true
                }
            },
            dist: {
                files: {
                    'website/site-static/js/app/<%= pkg.name %>.min.js': [
                        'website/web-apps/dist/controller/controllers.js',
                        'website/web-apps/dist/model/models.js'
                    ]
                }
            }
        },
        qunit: {
            files: ['test/**/*.html']
        },
        jshint: {
            files: ['Gruntfile.js', 'website/web-apps/src/**/*.js', 'test/**/*.js'],
            options: {
                // options here to override JSHint defaults
                globals: {
                    jQuery: true,
                    console: true,
                    module: true,
                    document: true
                }
            }
        },
        watch: {
            files: ['<%= jshint.files %>'],
            tasks: ['jshint', 'qunit']
        }
    });

    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-contrib-jshint');
    grunt.loadNpmTasks('grunt-contrib-qunit');
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-contrib-coffee');
    grunt.loadNpmTasks('grunt-ngmin');
    grunt.loadNpmTasks('grunt-contrib-compass');

    grunt.registerTask('test', ['jshint', 'qunit']);
    grunt.registerTask('style', ['compass']);

    grunt.registerTask('default', ['coffee', 'ngmin', 'uglify']);

};