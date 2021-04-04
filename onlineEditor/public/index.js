const compile = async () => {
    code = editorIn.getValue();
    button = document.querySelector('#compileButton');
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
        editorOut.setValue((await res.json()).compiledCode);
    } catch (e) {
        editorOut.setValue(e);
    }

    button.disabled = false;
    button.innerHTML = 'Compile';
}