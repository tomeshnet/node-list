require 'json-schema'

schema_version = ENV['SCHEMA_VERSION']

describe 'nodeList.json' do
  it "conforms to v#{schema_version}/schema.json" do
    schema_file = File.expand_path("../schema/v#{schema_version}/schema.json", File.dirname(__FILE__))
    nodelist_file = File.expand_path('../nodeList.json', File.dirname(__FILE__))
    JSON::Validator.validate!(schema_file, nodelist_file)
  end
end