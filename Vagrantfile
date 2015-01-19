# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

VAGRANT_LOCAL_CONFIG = "vagrant-conf.local"

load(VAGRANT_LOCAL_CONFIG) if File.exist?(VAGRANT_LOCAL_CONFIG) # include local configuration if available 

VAGRANT_ARCH = "x64" unless defined? VAGRANT_ARCH

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
    config.vm.define "liberator" do |liberator|
        if VAGRANT_ARCH == "x64"
            liberator.vm.box = "debian" 
            liberator.vm.box_url = "ftp://ftp.lugons.org/vagrant/debian-7.6.0-x86_64.box"  
	else 
	    liberator.vm.box = "chef/debian-7.6-i386"
	end 

        liberator.vm.network :private_network, ip: "192.168.66.6"
        liberator.vm.provision :ansible do |ansible|
            ansible.playbook = "provision/site.yml"
            ansible.host_key_checking = false
            ansible.groups = {
                "vagrant" => ["liberator"],
            }
        end
    end
end
