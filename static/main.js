document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('uploadForm');
    const fileInput = document.getElementById('fileInput');
    const resultDiv = document.getElementById('result');

    form.addEventListener('submit', async function(e) {
        e.preventDefault();
        resultDiv.innerHTML = '';
        const file = fileInput.files[0];
        if (!file) {
            resultDiv.innerHTML = '<span class="error">Please select a file.</span>';
            return;
        }
        const conversionType = document.querySelector('input[name="conversionType"]:checked').value;
        const reader = new FileReader();
        reader.onload = async function() {
            const arrayBuffer = reader.result;
            try {
                await eel.save_upload(file.name, Array.from(new Uint8Array(arrayBuffer)))();
                const response = await eel.convert_file(file.name, conversionType)();
                if (response.success) {
                    const downloadUrl = `/static/${response.output_file}`;
                    resultDiv.innerHTML = `<a href="${downloadUrl}" download>Download Converted File</a>`;
                } else {
                    resultDiv.innerHTML = `<span class="error">${response.error}</span>`;
                }
            } catch (err) {
                resultDiv.innerHTML = `<span class="error">Error: ${err}</span>`;
            }
        };
        reader.readAsArrayBuffer(file);
    });
});
