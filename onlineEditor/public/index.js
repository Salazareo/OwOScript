const fakeOutput = (toPrint) => {
    editorShell.setValue(editorShell.getValue() + toPrint + '\n');
}

const compile = async () => {
    const code = editorIn.getValue();
    const button = document.querySelector('#compileButton');
    button.disabled = true;
    button.innerHTML = 'Compiling...';
    try {
        const res = await fetch('api/compile', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                code
            }),
        });
        if (res.status !== 200) {
            throw new Error((await res.json()).error);
        }
        const { compiledCode, AST } = (await res.json());
        editorOut.setValue(compiledCode);
        editorAST.setValue(AST);


    } catch (e) {
        console.log(e);
        editorOut.setValue(e.message || e.toString());
    }

    button.disabled = false;
    button.innerHTML = 'Compile';
}


const runCode = () => {
    editorShell.setValue('');
    document.getElementById('exec')?.remove();
    const code = editorOut.getValue();
    const myScript = document.createElement("script");
    myScript.id = 'exec';
    myScript.innerHTML = `(()=>{${code.replaceAll('console.log', 'fakeOutput')}})()`
    document.body.appendChild(myScript);
}