import {
    window as vWindow,
    ViewColumn,
    ExtensionContext,
    WebviewPanel,
} from 'vscode';

import {
    Options,
    PythonShell,
    PythonShellError
} from 'python-shell'

type Response = {
    text: string
    length: number
}

export class Previewer {

    private context_: ExtensionContext;
    private panel_: WebviewPanel;
    private options_: Options;
    private response_: Response;

    constructor(context: ExtensionContext) {
        this.context_ = context;
        this.panel_ = vWindow.createWebviewPanel(
            'preview',
            'プレビュー',
            ViewColumn.One,
            {}
        );
        this.options_ = {
            ...PythonShell.defaultOptions,
            mode: 'text',
            scriptPath: __dirname
        }
        this.response_ = {
            text: '',
            length: 0
        }
    }

    private setArg(arg: string) {
        console.log(typeof arg)
        if(Array.isArray(this.options_.args)) {
            this.options_.args.push(arg)
        }else{
            this.options_.args = [arg]
        }
    }

    private setText(aText: string) {
        console.log('入力：', aText)
        const length = aText.length
        const aString = aText.slice(this.response_.length)
        this.response_.text = aString
        this.response_.length = length
        console.log('代入：', aString, length)
        console.log('出力：', this.response_)
    }

    private execute(scriptPath: string, options: Options, callback: (err?: PythonShellError | null, output?: Array<any> | null) => any) {
        let pyshell = new PythonShell(scriptPath, options);
        const output: Array<any> = new Array<any>();
        console.log('初期値')
        console.log(output)

        pyshell.on('message', function (message) {
            // console.log(output)
            output.push(message);
        }).end(function (err: PythonShellError | null) {
            return callback(err ? err : null, output.length ? output : null);
        });
        console.log('戻り値')
        console.log(output)
        return output
    };

    private run(script: string) {
        const pyShell = new PythonShell(script, this.options_)
        // let output: Array<string> = []
        // pyShell.on('message', (message) => {
        //     output.push(message)
        //     // console.log(message, output)
        // }).end((err: PythonShellError, exitCode: number=output.length, exitSignal: string): any => {
        //     if(err !== undefined) {
        //         throw err
        //     }
        // })
        // console.log(output)
        // this.setText(output.join('<br/>'))
        const resp = this.execute(script, this.options_, (err, res) => {
            console.log('err:')
            console.log(err)
            console.log('-----')
            console.log('res:')
            console.log(res)
        })
        console.log()
        console.log('response:')
        console.log(resp)
        // PythonShell.run(script, this.options_, (err, res) => {
        //     console.log(err, res)
        //     console.log('未更新:', this.response_)
        //     if(err) {
        //         console.error(err)
        //         throw err
        //     }
        //     // const res_str: string = (res || [''])[0]
        //     this.setText(res === undefined? '': res.join('<br/>'))
        // })
    }

    public update() {
        let editor = vWindow.activeTextEditor;
        if(editor?.document){
            this.setArg(editor.document.getText())
            this.run('./translator/execute.py')
        }
        console.log('response:')
        console.log(this.response_)
        this.panel_.webview.html = `<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Cat Coding</title>
        </head>
        <body>
            <h1>こんにちは日本</h1>
            <code style="display: block;white-space: pre-wrap">${this.response_.text}</code>
        </body>
        </html>`;
    }
}