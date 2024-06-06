from flask import Flask

def create_app():
    app = Flask(__name__)

    # Import and register blueprints
    from .routes.project import project_bp
    from .routes.environment import environment_bp
    from .routes.interface import interface_bp
    from .routes.intercase import intercase_bp
    from .routes.scene import scene_bp
    from .routes.scenetocase import scenetocase_bp
    from .routes.task import task_bp
    from .routes.report import report_bp


    #注册蓝图
    app.register_blueprint(project_bp, url_prefix='/project')
    app.register_blueprint(environment_bp, url_prefix='/environment')
    app.register_blueprint(interface_bp,url_prefix='/interface')
    app.register_blueprint(intercase_bp, url_prefix='/intercase')
    app.register_blueprint(scene_bp, url_prefix='/scene')
    app.register_blueprint(scenetocase_bp, url_prefix='/scenetocase')
    app.register_blueprint(task_bp, url_prefix='/task')
    app.register_blueprint(report_bp, url_prefix='/report')

    return app
