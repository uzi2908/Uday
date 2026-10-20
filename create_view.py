from flask import Flask, render_template_string


def creating_view(app : Flask):
    @app.route('/' , methods=['GET'])
    def home():
        return render_template_string(
            """
            <h1>
I am returning this view from the view application 
</h1>
            """
            
        )
