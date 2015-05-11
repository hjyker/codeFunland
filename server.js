var http = require('http');
var fs = require("fs");
var exec = require("child_process").exec;
var querystring = require("querystring");

function on_request (request, response) {
    var body = [];
    // console.log(request.method);
    // console.log(request.headers);
    console.log(request.url);
    response.writeHead(200, {
        'Content-Type': 'text-plain',
        "Access-Control-Allow-Origin": '*'
    });

    if (request.method == "GET") {
        response.write("Wow,woW\nHey guys, What's up?");
        response.end();

    } else { // if post
        request.on('data', function (post_data) {
            body.push(post_data);
        });

        request.on('end', function () {
            body = Buffer.concat(body);
            params = handle_post_params(body);
            file_path = "/home/code/work/" + params.code_file_name;

            fs.writeFile(file_path, params.code_content, "utf-8", function (err) {
                if (err) throw err;
            });
            comment = params.command_pre + ' ' + file_path;
            // console.log(comment);
            exec_comment(response, comment);
        });
    }
}

function handle_post_params (body) {
    params = querystring.parse(body.toString());

    return {
        code_file_name: params.code_path.split('/').slice(-1).toString(),
        command_pre: params.command_pre.toString(),
        code_content: params.code_content
    };
}

function exec_comment(response, comment) {
    var opts = {
        encoding: 'utf8',
        timeout: 1000, // one second
        maxBuffer: 100 * 1024,
        killSignal: 'SIGTERM',
        cwd: "/home/code/work",
        env: null
    };
    exec(comment, opts, function (error, stdout, stderr) {
        if (error) {
            // response.write(error.toString());asynchronous callback pattern in javascript
            // response.write('Server Error!\n');
            // throw error;
        }

        if (stdout) {
            // response.write('stdout:');
            response.write(stdout);
            console.log(stdout);
        }

        if (stderr) {
            // response.write('stderr:');
            response.write(stderr);
            console.log(stderr);
        }
        response.end();
    });
}

http.createServer(on_request).listen(9999);

