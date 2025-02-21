from marshmallow import Schema, fields

class ProjectSchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)
    description = fields.Str(required=True)
    technologies = fields.List(fields.Str(), required=True)
    start_date = fields.Date(required=True)
    end_date = fields.Date(required=True)