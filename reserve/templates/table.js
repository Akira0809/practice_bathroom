let selectedTime = null;

function selectTime(time) {
    selectedTime = time;
}

for (let i = 16; i < 22; i++) {
    for (let j = 0; j < 60; j += 30){
        const time = `${i.toString().padStart(2, '0')}:${j.toString().padStart(2, '0')}`;
        document.write(`
            <tr>
                <td class="py-2 px-4 text-center border border-gray-300">${time}</td>
                <td class="py-2 px-4 text-center border border-gray-300">
                    <input type='submit' name='reservation' value='${time}-4人' onclick="selectTime('${time}')">
                </td>
                <td class="py-2 px-4 text-center border border-gray-300">
                    <input type='submit' name='reservation' value='${time}-9人' onclick="selectTime('${time}')">
                </td>
            </tr>
        `);
    }
}
