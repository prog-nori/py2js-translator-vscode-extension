"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.Previewer = void 0;
const vscode_1 = require("vscode");
const python_shell_1 = require("python-shell");
const child_process_1 = require("child_process");
class Previewer {
    constructor(context) {
        this.context_ = context;
        this.panel_ = vscode_1.window.createWebviewPanel('preview', 'プレビュー', vscode_1.ViewColumn.One, {});
        this.options_ = Object.assign(Object.assign({}, python_shell_1.PythonShell.defaultOptions), { mode: 'text', scriptPath: __dirname, pythonPath: 'python3' });
        this.response_ = {
            text: '',
            length: 0
        };
    }
    setArg(arg, reset = false) {
        console.log(typeof arg);
        if (Array.isArray(this.options_.args) && reset === false) {
            this.options_.args.push(arg);
        }
        else {
            this.options_.args = [arg];
        }
    }
    run(script) {
        return __awaiter(this, void 0, void 0, function* () {
            const args = this.options_.args ? this.options_.args : [];
            const target = `${__dirname}/${script}`;
            const python = child_process_1.spawn('python', [target, args.join(' ')]);
            const chunks = new Array();
            return new Promise((resolve, reject) => {
                python.stdout.on('data', (chunk) => {
                    chunks.push(Buffer.from(chunk));
                });
                python.stderr.on('data', (data) => {
                    console.error(`stderr: ${data}`);
                    reject(data);
                });
                python.on('exit', () => {
                    resolve(Buffer.concat(chunks).toString('utf-8'));
                });
            });
        });
    }
    update() {
        let editor = vscode_1.window.activeTextEditor;
        if (editor === null || editor === void 0 ? void 0 : editor.document) {
            this.setArg(editor.document.getText(), true);
            // old
            // this.run('translator/execute.py').then(res => {
            this.run('py2js/py2js.py').then(res => {
                console.log('async log:', res);
                this.response_.text = String(res);
            });
        }
        console.log('response:');
        console.log(this.response_);
        this.panel_.webview.html = `<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Cat Coding</title>
        </head>
        <body style="white-space: pre">
            ${this.response_.text}
            <!-- <code style="display: block;white-space: pre-wrap">${this.response_.text}</code> -->
        </body>
        </html>`;
    }
}
exports.Previewer = Previewer;
//# sourceMappingURL=previewer.js.map