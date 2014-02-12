
function getStateUpdateFunctions()
{
    var step1 = function(state) {
        state.x = 3
    }
    var step2 = function(state) {
        state.y = 5
    }
    var step3 = function(state) {
        state.result = (state.x * state.y)
    }
    var step4 = function(state) {
        state.y += 1
    }
    var step5 = function(state) {
        state.result *= state.x + state.y
    }

    return [step1, step2, step3, step4, step5]
}

function createProgramState()
{
    var state = {
        /// this is the actual state of the program being traced
        x: 0,
        y: 0,
        result: 0,
        /// this is the state of the program tracer
        stateXformers: getStateUpdateFunctions(),
        step: 0,
        executeNextStatement: function() {
            this.stateXformers[this.step](this)
            ++this.step
        },
        toString: function() {
            return "{ x: " + this.x + ", y: " + this.y + ", result: " + this.result + " }"
        }
    }

    return state
}

function createProgram(stat_block_id, state)
{
    var program = {
        stat_block_id: stat_block_id,
        state: state,
        statement: null,
        executeNextStatement: function() {
            if (this.statement.previousElementSibling) {
                this.statement.previousElementSibling.classList.remove('active');
            }
            this.statement.classList.add('active');
            console.log(this.statement.innerText.trim())
            this.state.executeNextStatement()
            console.log("    ", this.state.toString())
            var next_statement = this.statement.nextElementSibling
            if (next_statement) {
                this.statement = next_statement
                window.setTimeout(this.executeNextStatement.bind(this), 1800)
            }
        },
        run: function() {
            console.log("initial state: ", this.state.toString())
            var block = document.getElementById(this.stat_block_id)
            this.statement = block.firstElementChild
            window.setTimeout(this.executeNextStatement.bind(this), 200) 
        },
        
        display: function() {
            console.log(this.x, this.y, this.result)
        }
    }
    return program
}


function main()
{
    var pt = createProgram("statement_block", createProgramState())
    pt.run()
}

addEventListener("load", main)
