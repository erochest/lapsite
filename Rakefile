
require 'etc'
require 'fileutils'
require 'vagrant'


task :default => :usage

task :usage do
  puts "You forgot to tell the computer what to do; try one of these commands:"
  system("rake -T")
end

# Execute a command in the primary VM and write its output to the screen.
def vm_ssh(env, cmd)
  puts ">>> '#{cmd}'"
  env.primary_vm.ssh.execute do |ssh|
    ssh.exec!(cmd) do |channel, stream, data|
      print data
      $stdout.flush
    end
  end
end

desc 'Destroys and initializes the environment.'
task :init => [:clobber,
               :cookbooks,
               'vm:up']

desc 'Cleans everything out of the environment.'
task :clobber do
  FileUtils.rmtree %w{omeka omeka.bk cookbooks}, :verbose => true
  env = Vagrant::Environment.new
  if env.primary_vm.created?
    puts 'vagrant destroy'
    env.cli('destroy')
  end
end

desc 'Downloads the cookbooks.'
task :cookbooks do
  Dir.mkdir("cookbooks") unless File.directory?("cookbooks")
  system('git clone --branch=slab https://github.com/erochest/opscode-cookbooks.git cookbooks/opscode')
  system('git clone https://github.com/scholarslab/cookbooks.git cookbooks/slab')
end

namespace :vm do
  desc 'This calls Vagrant up.'
  task :up do
    env = Vagrant::Environment.new
    puts 'vagrant up'
    env.cli('up')
  end

  desc 'Do a safe halt on the VM.'
  task :halt do
    vm_ssh(Vagrant::Environment.new, 'sudo halt')
  end

  desc "cat /tmp/vagrant-chef-1/chef-stacktrace.out."
  task :chefst do
    env = Vagrant::Environment.new
    raise "Must run `vagrant up`" if !env.primary_vm.created?
    raise "Must be running!" if !env.primary_vm.vm.running?
    puts "Getting chef stacktrace."
    vm_ssh(env, "cat /tmp/vagrant-chef-1/chef-stacktrace.out")
  end
end
