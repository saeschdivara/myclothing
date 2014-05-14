module.exports = function (grunt) {

    var style_path = 'website/site-static/style/'

    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        coffee: {
            compileJoined: {
                options: {
                    join: true
                },
                files: {
                    'website/web-apps/dist/controller/controllers.js': [
                        'website/web-apps/src/main.coffee',
                        'website/web-apps/src/controller/*.coffee'
                    ],
                    'website/web-apps/dist/model/models.js': [
                        'website/web-apps/src/model/*.coffee'
                    ]
                }
            }
        },
        uglify: {
            options: {
                banner: '/*! <%= pkg.name %> - v<%= pkg.version %> - ' +
                        '<%= grunt.template.today("yyyy-mm-dd")  %> copyright by <%= pkg.author %> */ \n',

                beautify: true,
                mangle: false,
                compress: {
                    drop_console: false
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
        compass: {                  // Task
            dist: {                   // Target

                outputStyle: 'nested',
                debugsass: true,
                options: {              // Target options
                    config: style_path + 'config.rb',
                    sassDir: style_path + 'sass',
                    cssDir: style_path + 'css',
                    environment: 'development'
                }
            }
        }
    });

    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-contrib-jshint');
    grunt.loadNpmTasks('grunt-contrib-qunit');
    grunt.loadNpmTasks('grunt-contrib-coffee');
    grunt.loadNpmTasks('grunt-contrib-compass');

    grunt.registerTask('test', ['jshint', 'qunit']);
    grunt.registerTask('style', ['compass']);

    grunt.registerTask('default', ['coffee', 'uglify']);

};