const student = {
  firstName: 'Greg',
  lastName: 'Focker',
  studentId: '234359',
  phone: '040 5902123',
  location: {
    city: "Espoo"
  },
  courses: [{
    name:"Ohjelmisto 1",
    completed: true
  },
    {
      name:"Ohjelmisto 2",
      completed: false
    }]
}

console.log(student['phone'])
console.log(student.phone)

console.log(student.courses[0].completed)
console.log(student.courses[1].completed)
console.log(student.location.city)

console.log(student['courses'][0]['completed'])
console.log(student['courses'][1]['completed'])
console.log(student['location']['city']);

const muuttuja = "hevonen"
console.log(`merkkijono ${muuttuja}`)
console.log('merkkijono ' + muuttuja)
console.log("merkkijono" + muuttuja)